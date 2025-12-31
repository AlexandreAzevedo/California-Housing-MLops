# 1. Start with a base box that has Python 3.9 installed
FROM python:3.12-slim

# 2. Create a folder inside the box to hold our app
WORKDIR /code

# 3. Copy the list of ingredients into the box
COPY ./requirements.txt /code/requirements.txt

# 4. Install the ingredients inside the box
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Copy our "Waiter" (API) and "Kitchen" (Model) code into the box
COPY ./app /code/app
COPY ./model /code/model

# 6. Open a "Window" (Port) so the world can talk to the app
EXPOSE 80

# 7. Tell the box what to do when it turns on: "Run the server"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]