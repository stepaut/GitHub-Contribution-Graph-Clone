from flask import Flask, render_template, json
import spreadsheet

SOURCE = "EXCEL"  # GDRIVE , EXCEL
THEME = "green"  # green , hard

app = Flask(__name__)


@app.route("/")
def main():
    if SOURCE == "GDRIVE":
        data = spreadsheet.getDataFromGoogleDrive()
        return render_template('gdrive.html', data=data, theme=THEME)
    elif SOURCE == "EXCEL":
        data = spreadsheet.getDataFromExcel()
        return render_template('excel.html', data=data, theme=THEME)
    else:
        return


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=5000, threaded=True)
