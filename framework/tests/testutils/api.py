import json

def api_verify(client, json_data):
    resp = client.post(
            '/api/verify',
            data=json.dumps(json_data),
            content_type='application/json',
            follow_redirects=True
        )
    data = json.loads(resp.data)
    print("\nVerify data:\n{}\n".format(str(data)))
    return data
