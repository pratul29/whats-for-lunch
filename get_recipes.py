import pickle
import json
import subprocess

reverse_index = pickle.load(open( "reverse_index.pickle", "rb" ))

f1 = open("detect.txt", "r")
f2 = open("result.txt", "w")

subprocess.run(["./darknet", "detector", "test", "../data_for_local/obj.data", 
"../data_for_local/obj.cfg", "../obj_2000.weights", "-i", "0", "-thresh", "0.1"], 
cwd="darknet", stdin = f1, stdout = f2)


# darknet detector test data_for_local/obj.data data_for_local/obj.cfg obj_2000.weights -i 0 -thresh 0.3 < detect.txt > result.txt

f = open("result.txt", "r")
predictions = f.readlines()
print(predictions)
query = set()
for prediction in predictions:
    if not prediction.startswith("Enter Image Path:"):
        ans = prediction[:prediction.index(':')]
        query.add(ans)

query = list(query)

result = set(reverse_index[query[0]])

for i in query:
	result = result & set(reverse_index[i])

print(result)

food_data = json.load(open("food_db.json", "r"))

answer = []
hash_ = set()
for r in result:
	for dish in food_data:
		if r == dish['dish_id'] and dish['url'] not in hash_:
			answer.append({'dish_name':dish['dish_name'], 'link' : dish['url'], 'ingredients' : dish['ingredients']})

			hash_.add(dish['url'])

print(query)

print(len(answer))

for i in answer:
    print(i['dish_name'])
    print(i['link'])
    print("=" * 40)
