# Instagram Clone Backend

This project implements the backend of an Instagram-like application using **FastAPI** and **MongoDB**. The backend exposes RESTful APIs for user authentication, post creation, following users, commenting, and retrieving user feeds.

## Features

### Mandatory Features:
1. **User Registration and Login**: Secure user authentication using JWT.
2. **Create Posts**: Posts include captions, media URLs, optional music, categories, timestamps, and user references.
3. **View User Profiles**: Retrieve user details including followers, following, and their posts.
4. **Follow Users**: Users can follow/unfollow others.
5. **Post Retrieval**:
   - Get posts of logged-in users.
   - Get posts by other users.
   - Retrieve details of specific posts.
6. **Post Interactions**:
   - Like posts.
   - View users who liked a post.
   - Comment on posts.
   - View comments on a post.
7. **User Feed**: Retrieve posts from followed users in reverse chronological order with pagination.

### Bonus Features:
- Placeholder for potential bonus features like search, notifications, or analytics.

---

## Project Setup

### Prerequisites:
1. **Python** (version 3.9 or higher).
2. **MongoDB** installed locally or accessible remotely.
3. A virtual environment for Python (optional but recommended).

### Installation Steps:

#### 1. Clone the Repository:
```bash
git clone https://github.com/your-repo/instagram-clone-backend.git
cd instagram-clone-backend
```

#### 2. Set Up a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate     # On Windows
```

#### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables:
Create a `.env` file in the root directory with the following contents:
```plaintext
DATABASE_URL=""
SECRET_KEY=""
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
#### 5. Initialize the Database:
Ensure MongoDB is running locally or remotely. The required collections (`users`, `posts`, and `comments`) will be automatically created when data is added.

#### 6. Start the Application:
Run the application using Uvicorn:
```bash
uvicorn app.main:app --reload
```
The server will start at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Authentication:
1. **Register User**:
   - **Endpoint**: `POST /auth/register`
   - **Body**:
     ```json
     {
         "username": "string",
         "email": "string",
         "password": "string"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "User registered successfully."
     }
     ```

2. **Login User**:
   - **Endpoint**: `POST /auth/login`
   - **Body**:
     ```json
     {
         "email": "string",
         "password": "string"
     }
     ```
   - **Response**:
     ```json
     {
         "access_token": "string",
         "token_type": "bearer"
     }
     ```

### Users:
1. **View Profile**:
   - **Endpoint**: `GET /users/{user_id}`
   - **Response**: Returns user details and posts.

2. **Follow User**:
   - **Endpoint**: `POST /users/{user_id}/follow`
   - **Body**:
     ```json
     {
         "follower_id": "string"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "Followed successfully."
     }
     ```

### Posts:
1. **Create Post**:
   - **Endpoint**: `POST /posts/`
   - **Body**:
     ```json
     {
         "caption": "string",
         "media_url": "string",
         "music_url": "string (optional)",
         "category": "string",
         "publisher_id": "string"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "Post created successfully."
     }
     ```

2. **Get Post**:
   - **Endpoint**: `GET /posts/{post_id}`
   - **Response**: Returns post details, likes count, and comments count.

3. **Like Post**:
   - **Endpoint**: `POST /posts/{post_id}/like`
   - **Response**:
     ```json
     {
         "message": "Post liked successfully."
     }
     ```

4. **Comment on Post**:
   - **Endpoint**: `POST /posts/{post_id}/comment`
   - **Body**:
     ```json
     {
         "user_id": "string",
         "text": "string"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "Comment added successfully."
     }
     ```

5. **User Feed**:
   - **Endpoint**: `GET /feed/`
   - **Query Parameters**: `page`.
   - **Response**: Returns paginated posts of followed users.

---


## Additional Notes
- **Error Handling**: Errors return standardized JSON responses with appropriate HTTP status codes.
- **Security**: Ensure environment variables are secure and not hardcoded.
- **Scalability**: MongoDB is used to handle large datasets with flexible schemas.

---
