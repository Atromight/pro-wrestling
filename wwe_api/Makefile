ENTRY_POINT := "wwe_api.main:app"
SERVER_PORT := 8080

run:
	poetry run uvicorn --host 0.0.0.0 --port ${SERVER_PORT} --reload ${ENTRY_POINT}

clean:
	rm -rf wwe_api/__pycache__ 