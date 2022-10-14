from flask import Flask, render_template, jsonify, redirect, url_for
import json

def create_app():
    app = Flask(__name__)
    
    from .views import graph_views, homepage_views, data_views, controller_views
    
    app.register_blueprint(homepage_views.bp) # 전체적인 페이지 관리 (navibar)
    app.register_blueprint(graph_views.bp)
    app.register_blueprint(data_views.bp)
    app.register_blueprint(controller_views.bp)

    return app