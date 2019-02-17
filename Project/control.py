from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

	item1 = request.form['item1']
	item2 = request.form['item2']
	item3 = request.form['item3']
	#print(item1)
	#print(item2)
	#print(item3)

	input = []
	
	input.append(item1)
	input.append(item2)
	input.append(item3)
	
	f = open('formattedData.json')
	
	
	data = json.load(f)
	f.close()

	jobs = [] #all jobs
	
#add all jobs
	for(k,v) in data.items():
		job = [] #that job
		job.append(k) #title 0
		job.append(v[1]) #link 1
		job.append(v[0]) #company 2
		job.append(v[2]) #list of tags 3
		points = 0
		for i in range(0,len(v[2])):
			for j in range(0,len(input)):
				print(input[j]+":"+v[2][i])
				if input[j].lower()==v[2][i]:
					print("+1")
					points += 1
		job.append(points)#relevant 4
		jobs.append(job)
	
	for x in range(len(jobs)-1,0,-1):
		for y in range(x):
			if jobs[y][4]>jobs[y+1][4]:
				temp = jobs[y]
				jobs[y] = jobs[y+1]
				jobs[y+1] = temp

	
	jobs.reverse()
	
	#items.append(item1)
	#items.append(item2)
	#items.append(item3)

	return render_template('result.html', jobs = jobs)
	#return render_template('result.html', name=name, comment=comment)


if __name__ == '__main__':
	app.run(debug=True)