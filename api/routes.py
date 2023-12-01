from ast import Raise
from flask import Response, json, request, abort, jsonify, session
import pprint
from services.Extraction import ExtractionService
from ports.spicyEntityExtractor import spicyEntityExtrator
from models import apiResult

def get_routes(app):
###
# Rutas definidas para status, importa las funciones de api.status (/api/status.py)
###
    @app.route("/status/ping", methods=["GET"])
    def get_ping():

        return jsonify("pong")

    @app.route("/status/ready", methods=["GET"])
    def get_ready():
        return jsonify("Ready")
    @app.route("/api/extract", methods=["POST"])
    def extract():
        _result = apiResult.apiResult()
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            post_body = request.json
        else:
            _result.code = "400"
            _result.description = "Bad Request - Incorrect Body Format"            
            return _result.toJSON(), int(_result.code)


        _service = ExtractionService()
        _extractor = spicyEntityExtrator()
        _text = post_body["text"]

        try:
            extractionDict = _service.doExtraction(_text,_extractor)
            _result.code = "200"
            _result.description = ""
            _result.result = extractionDict.result()
        except Exception as e:
            _result.code = "500"
            _result.description = e

        return _result.toJSON(), int(_result.code)
