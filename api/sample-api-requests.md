# Sample API Requests

## GET Devices

```bash
curl http://localhost:5000/devices
```

Expected result:

```json
[
  {
    "devIP": "192.168.56.101",
    "devName": "CSR1kv-01",
    "devType": "router"
  }
]
```

## POST Device

```bash
curl -X POST http://localhost:5000/devices \
  -H "Content-Type: application/json" \
  -d '{"devIP":"192.168.56.102","devName":"CSR1kv-02","devType":"router"}'
```

## DELETE Device

```bash
curl -X DELETE http://localhost:5000/devices/192.168.56.102
```

## Notes

Update the hostname, IP address, or port based on the environment where the Flask API is running.
