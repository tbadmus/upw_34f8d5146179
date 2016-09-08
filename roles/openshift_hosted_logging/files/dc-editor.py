import json

with open('/tmp/dc-es.json') as f:
    data = json.load(f)

data['spec']['template']['spec']['containers'][0]['volumeMounts'] = [{'readOnly': True, 'name': 'elasticsearch', 'mountPath': '/etc/elasticsearch/keys'}, {'name': 'elasticsearch-nfs', 'mountPath': '/elasticsearch/persistent'}]

data['spec']['template']['spec']['volumes'] = [{'name': 'elasticsearch', 'secret': {'secretName': 'logging-elasticsearch'}}, {'name': 'elasticsearch-nfs', 'persistentVolumeClaim': {'claimName': 'es-claim'}}]

with open('/tmp/dc-es.json', 'w') as f:
    json.dump(data, f)
