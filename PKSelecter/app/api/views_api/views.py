from flask import render_template


# circular import 방지를 위해 deco함수를 만들었다
def views_router(views_bp):
    @views_bp.route("/")
    def main_view_api():

        print("views api inner")
        return render_template("pkselect.html")
    
    @views_bp.route("/privacy")
    def privacy_view_api():
        return render_template("PKselcet처리방침.html")
