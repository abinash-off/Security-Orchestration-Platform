from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
PLAYBOOKS={"triage_alert":["validate alert","collect metadata","create investigation note"],"isolate_endpoint":["record endpoint","simulate isolation","create analyst task"]}
@app.get("/")
def home(): return render_template("index.html",playbooks=PLAYBOOKS)
@app.post("/api/run")
def run():
 d=request.get_json(silent=True) or {}; name=d.get("playbook"); 
 if name not in PLAYBOOKS:return jsonify(error="unknown playbook"),404
 return jsonify(playbook=name,status="SIMULATED",steps=[{"step":s,"status":"completed"} for s in PLAYBOOKS[name]])
@app.get("/api/playbooks")
def playbooks(): return jsonify(PLAYBOOKS)
if __name__=="__main__":app.run(debug=True)