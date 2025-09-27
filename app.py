#!/usr/bin/env python3
from flask import Flask, request, Response, render_template, url_for, send_file
import os, re, sys, io
from profanity_filter import ProfanityFilter

import CARL

PREFIX = os.environ.get('PREFIX', '') #e.g. /carl
PORT = int(os.environ.get('PORT', '8080'))

pf = ProfanityFilter()
app = Flask(__name__, static_url_path=PREFIX + '/static')

@app.route(PREFIX+"/profanity-check")
def profanity_check():
    return pf.censor("That's bullshit!")

@app.route(PREFIX+"/api", methods=["GET", "POST"])
def carl_api():
    carl = request.args.get("carl", "")
    user = request.args.get("user", "")
    allowProfanity = request.args.get("profanity", "") == "true"

    answer = CARL.answer(carl, user, allowProfanity)
    return Response(answer, mimetype='text/plain')

@app.route(PREFIX if PREFIX != '' else '/', methods=["GET", "POST"])
def carl_page():
    carl = request.args.get("carl", "")
    user = request.args.get("user", "")
    allowProfanity = request.args.get("profanity", "") == "true"

    carl2 = CARL.answer(carl, user, allowProfanity)

    return render_template(
        "carl.html",
        allowProfanity=allowProfanity,
        carl=carl,
        user=user,
        carl2=carl2
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
