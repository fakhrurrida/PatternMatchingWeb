import os
from app.processing_bois.regeks import *
from app.processing_bois.boyer_moore import *
from app.processing_bois.kmp import *
from app import app
from flask import render_template, flash, request, redirect

app.config["IMAGE_UPLOADS"] = 'C:\\Users\\windows\\Desktop\\OOP\\app\\app\\static\\uploaded'
app.config["ALLOWED_FILE"] = ["TXT"]

def allowed_file(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".",1)[1]
    if ext.upper() in app.config["ALLOWED_FILE"]:
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if request.files:
            image = request.files.getlist("text")
            print(image)
            for news in image:
                news.save(os.path.join(app.config["IMAGE_UPLOADS"], news.filename))
            #return redirect(request.url)
    return render_template("upload_file.html")

@app.route("/upload-file-subm", methods=["POST"])
def extractFiles():
    op = []
    os.chdir('C:\\Users\\windows\\Desktop\\OOP\\app\\app\\static\\uploaded')
    all_files = os.listdir('C:\\Users\\windows\\Desktop\\OOP\\app\\app\\static\\uploaded')
    pattern = request.form['pattern']
    algoritma = request.form['pilihanalgo']
    if algoritma == "kmp":
        print("kmp")
        print("pattern")
        algo = "KMP"
        for file in all_files:
            processed = tokenizedPassage(file)
            print(processed)
            print(filteredPassageKMP(pattern, processed))
            new = makeFinalArray(pattern, file, filteredPassageKMP(pattern, processed)).copy()
            op.append(new)
    elif algoritma == "bm":
        print("bm")
        algo = "BM"
        for file in all_files:
            processed = tokenizedPassage(file)
            print(processed)
            print(filteredPassageBM(pattern, processed))
            new = makeFinalArray(pattern, file, filteredPassageKMP(pattern, processed)).copy()
            op.append(new)
    elif algoritma == 'regex':
        print("regex")
        algo = "Regex"
        for file in all_files:
            processed = tokenizedPassage(file)
            print(processed)
            print(filteredPassageRE(pattern, processed))
            new = makeFinalArray(pattern, file, filteredPassageKMP(pattern, processed)).copy()
            op.append(new)
    # Hapus file yang ada di static/uploaded setelah pemrosesan teks
    for file in all_files:
        os.remove(file)
    print(pattern)
    return render_template("result.html", keyword = pattern, algo = algo, final = op)

@app.route("/about")
def about():
    return render_template("about_program.html")

@app.route("/whatiskmp")
def whatiskmp():
    return render_template("kmp.html")
    return "<h1 style='color: red'>Tentang program</h1>"

@app.route("/whatisbm")
def whatisbm():
    return render_template("boyer_moore.html")
    return "<h1 style='color: red'>Tentang program</h1>"

@app.route("/whatisre")
def whatisre():
    return render_template("regex.html")
    return "<h1 style='color: red'>Tentang program</h1>"