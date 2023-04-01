import os
import shutil
import vars_setup


def makeTempDir(path):
    if os.path.isfile(path):
        os.mkdir(vars_setup.newPath(vars_setup.dataBasePath, "temp"))
        shutil.copy(path, vars_setup.newPath(vars_setup.dataBasePath, "temp"))
        tempPath = vars_setup.newPath(vars_setup.dataBasePath, "temp")
        files = os.listdir(tempPath)
        files = list(files)
        filename = files[0]
        file = open(vars_setup.newPath(tempPath, "index.html"), "w")
        content = """
<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
		body {
			text-align: center;
			font-family: Arial, sans-serif;
			bg-color:#000;
		}
		
		.button {
			display: inline-block;
			background-color: #4CAF50;
			border: none;
			color: white;
			padding: 10px 20px;
			text-align: center;
			text-decoration: none;
			font-size: 16px;
			margin: 10px;
			cursor: pointer;
			border-radius: 5px;
		}
		
		@media (max-width: 768px) {
			/* styles for mobile devices */
			.button {
				display: block;
			}
		}
	</style>
</head>
<body class="body color="white">
	<h1>FTP Xenon v0.3</h1>
	<p>To get your file, tap on the below button.</p>
	<a href="/filename" download><button class="button">Download</button></a>
</body>
</html>
"""
        file.write(content.replace("filename", filename))
        file.close()
        os.system(f"start cmd /K python {vars_setup.newPath(vars_setup.dataBasePath, 'ftpxenon.py')}")

    if os.path.isdir(path):
        '''os.mkdir(vars_setup.newPath(vars_setup.dataBasePath, "temp"))
        shutil.make_archive(path,"zip",_dir=vars_setup.dataBasePath)
        tempPath = vars_setup.newPath(vars_setup.dataBasePath, "temp")
        files = os.listdir(tempPath)
        files = list(files)
        filename = files[0]
        file = open(vars_setup.newPath(tempPath, "index.html"), "w")
        content = """
        <!DOCTYPE html>
        <html>
        <head>
        	<meta name="viewport" content="width=device-width, initial-scale=1">
        	<style>
        		body {
        			text-align: center;
        			font-family: Arial, sans-serif;
        			bg-color:#000;
        		}

        		.button {
        			display: inline-block;
        			background-color: #4CAF50;
        			border: none;
        			color: white;
        			padding: 10px 20px;
        			text-align: center;
        			text-decoration: none;
        			font-size: 16px;
        			margin: 10px;
        			cursor: pointer;
        			border-radius: 5px;
        		}

        		@media (max-width: 768px) {
        			/* styles for mobile devices */
        			.button {
        				display: block;
        			}
        		}
        	</style>
        </head>
        <body class="body color="white">
        	<h1>FTP Xenon v0.3</h1>
        	<p>To get your file, tap on the below button.</p>
        	<a href="/my_archive.zip" download><button class="button">Download</button></a>
        </body>
        </html>
        """
        file.close()
        os.system(f"start cmd /K python {vars_setup.newPath(vars_setup.dataBasePath, 'ftpxenon.py')}")'''



def ftpStart(user):
    path = user[4:]
    makeTempDir(path)

