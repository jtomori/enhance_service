from flask import Flask, request, jsonify
from rq import Queue
from redis import Redis
from slow_job import slow_job

app = Flask(__name__)
app.config['DEBUG'] = True

redis_conn = Redis('localhost', 6379)
q = Queue(connection=redis_conn)

jobs = {}

@app.route('/job/get/<string:id>', methods=['GET',])
def getJobStatus(id):
    if id == "all":
        out_str = "number of jobs: {jobs_len} <br>job_ids: {job_ids}<br>jobs: {jobs}".format( jobs_len=str(len(q)), job_ids=q.job_ids, jobs=q.jobs )
        return out_str

    job = q.fetch_job(id)
    return job.get_status()

@app.route('/job/add', methods=['POST',])
def addJob():
    json_in = request.get_json()
    
    job = q.enqueue(slow_job, json_in["job"], result_ttl='1h')
    
    return job.get_id()

if __name__ == '__main__':
    app.run()