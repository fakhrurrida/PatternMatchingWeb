import re
TEXTO = "positif"
if (re.search(rf"\b(?=\w){TEXTO}\b(?!\w)", "Angka pOsItiF virus Corona atau COVID-19 di Jawa Barat menembus angka 400 kasus.", re.IGNORECASE)):
    print("Ada Pattern")
else:
    print("Not Found")

<div class="file-field">
      <div class="btn btn-primary btn-sm float-">
        <input type="file" accept=".txt" multiple="" name="files[]">
      </div>
    </div>
    <button type="submit" class="btn btn-primary">Submit Files</button>

if request.method == "POST":
        if request.files:
            files = request.files.getlist("file[]")
            for file in files:
                if file and allowed_file(file.filename):
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                print(file)
    return render_template("upload_file.html")