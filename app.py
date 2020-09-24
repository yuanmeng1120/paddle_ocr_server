from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse

from ocr_center.paddle_ocr import get_ocr_answer

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)


@app.route('/api/v1/ocr', methods=['POST'])
def do_search_api():
    args = reqparse.RequestParser(). \
        add_argument("urls", type=str). \
        add_argument("base64", type=str). \
        parse_args()
    if "urls" in args.keys():
        urls = args['urls']
        output = get_ocr_answer(urls=urls)
        if output:
            return {"output": output}
    if "base64" in args.keys():
        base64 = args['base64']
        output = get_ocr_answer(base64=base64)
        if output:
            return {"output": output}
    return "not found", 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2020)