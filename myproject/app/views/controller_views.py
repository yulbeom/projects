from flask import Blueprint, render_template, jsonify, request, redirect, url_for, jsonify
import sqlite3
import os

bp = Blueprint('controller', __name__, url_prefix='/')

