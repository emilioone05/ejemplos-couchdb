# Proceso de importación

1. Crear una base llamada demo2
2. Usar el siguiente comando

```
  curl -u admin:admin -d @demo2_import.json -H "Content-type: application/json" -X POST http://127.0.0.1:5984/demo2/_bulk_docs
```
