from app import create_app
#npx tailwindcss -i ./app/static/src/input.css -o ./app/static/dist/output.css --watch

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)