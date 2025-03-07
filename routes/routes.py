from flask import Blueprint, request, jsonify
from config.database import get_db_connection

krs_bp = Blueprint("krs", __name__)

# GET - ALL krs
@krs_bp.route("/krs", methods=["GET"])
def get_krs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id_krs, nim, "kode matakuliah", matakuliah, semester, tahunakademik FROM krs ORDER BY id_krs ASC LIMIT 2000000')
    krs = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"meta" : { "code": 200, "message" : "Success"}, "data" : [{"id_krs": u[0], "nim": u[1], "kode matakuliah": u[2], "matakuliah" : u[3], "semester" : u[4], "tahunakademik" : u[5]} for u in krs]})

# POST - ADD USER
@krs_bp.route("/krs", methods=["POST"])
def add_user():
    data = request.get_json()
    nim = data.get("nim")
    kode_matakuliah = data.get("kode matakuliah")
    matakuliah = data.get("matakuliah")
    semester = data.get("semester")
    tahunakademik = data.get("tahunakademik")
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO krs (nim, "kode matakuliah", matakuliah, semester, tahunakademik) VALUES (%s, %s, %s, %s, %s) RETURNING id_krs', (nim, kode_matakuliah, matakuliah, semester, tahunakademik))
    krs_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"meta" : { "code": 201, "message" : "Success"}, "data" : {"id_krs" : krs_id, "nim" : nim, "kode matakuliah": kode_matakuliah, "matakuliah" : matakuliah, "semester" : semester, "tahunakademik" : tahunakademik}}), 201

# GET - USER BY ID
@krs_bp.route("/krs/<int:krs_id>", methods=["GET"])
def get_user(krs_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT nim, "kode matakuliah", matakuliah, semester, tahunakademik FROM krs WHERE id_krs = %s', (krs_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    
    if user:
        return jsonify({"meta" : {"status": 200, "message" : "Success"},"data": {"id_krs": krs_id, "nim": user[0], "kode_matakuliah": user[1], "matakuliah": user[2], "semester": user[3], "tahunakademik": user[4]}})
    else:
        return jsonify({"code" : 404,"message": "KRS not found"}), 404

# PUT - UPDATE USER
@krs_bp.route("/krs/<int:krs_id>", methods=["PUT"])
def update_user(krs_id):
    data = request.get_json()
    nim = data.get("nim")
    kode_matakuliah = data.get("kode matakuliah")
    matakuliah = data.get("matakuliah")
    semester = data.get("semester")
    tahunakademik = data.get("tahunakademik")
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE krs SET nim = %s, "kode matakuliah" = %s, matakuliah = %s, semester = %s, tahunakademik = %s WHERE id_krs = %s RETURNING id_krs', (nim, kode_matakuliah, matakuliah, semester, tahunakademik, krs_id))
    updated = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    if updated:
        return jsonify({"meta": {"code": 204, "message": "Success"},"data" : {"id_krs" : krs_id, "nim" : nim, "kode matakuliah": kode_matakuliah, "matakuliah" : matakuliah, "semester" : semester, "tahunakademik" : tahunakademik}})
    else:
        return jsonify({"code": 404,"message": "KRS not found"}), 404

# DELETE - DELETE USER
@krs_bp.route("/krs/<int:krs_id>", methods=["DELETE"])
def delete_user(krs_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM krs WHERE id_krs = %s RETURNING id_krs", (krs_id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    if deleted:
        return jsonify({"code": 204,"message": "Success"})
    else:
        return jsonify({"code": 404,"message": "KRS not found"}), 404