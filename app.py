from flask import Flask, render_template, json
import spreadsheet

SOURCE = "CSV"  # GDRIVE , EXCEL , CSV
THEME = "green"  # green , hard

app = Flask(__name__)


@app.route("/")
def main():
    if SOURCE == "GDRIVE":
        data = spreadsheet.getDataFromGoogleDrive()
        return render_template('v1.html', data=data, theme=THEME)
    elif SOURCE == "EXCEL":
        data = spreadsheet.getDataFromExcel()
        return render_template('v2.html', data=data, theme=THEME)
    elif SOURCE == "CSV":
        data = spreadsheet.getDataFromCsv()
        if data is not None:
            return render_template('v2.html', data=data, theme=THEME)
    
    return render_template('oops.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=5000, threaded=True)
