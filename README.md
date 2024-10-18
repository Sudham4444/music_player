# Music Player 🎵

This is a simple Django-based music player web application that allows users to search for songs, view details like the artist, album, and thumbnail, and play songs directly from the app.

## 🌐 Live Demo

You can check out the live version of the app hosted on Vercel here: **[Live Demo](https://musicplayer-brown-theta.vercel.app/)**

> **Note:** Due to Vercel's limitations on serving media files, songs won't play on the live demo. For full functionality, please install and run the app locally by following the instructions below.

## 🎯 Features

- **Search for songs** by name or artist.
- **View song details** like album, artist, and thumbnail.
- **Play and pause songs** (works when installed locally).
- Responsive design that works well on both mobile and desktop.

## 🖼️ Project Snapshot (Local Version)

Below is a snapshot of the project running locally:

![Music Player Snapshot](https://github.com/Sudham4444/music_player/blob/main/music_player.png)

> Songs play perfectly fine when running locally.

## 🐛 Known Issue (Live Demo)

**Media Files Not Playing on Vercel**: Since Vercel uses an ephemeral file system, media files (like songs) are not persisted. As a result, songs do not play on the live demo. To experience the app's full functionality, you need to run it locally.

## 🚀 Running the App Locally

To experience the full functionality, you can run the project on your local machine. Follow these steps:

### 1. Clone the repository
    git clone https://github.com/Sudham4444/music_player.git
    cd music_player

### 2. Set up a virtual environment
It's recommended to use a virtual environment for Python projects.

    python -m venv env
    source env/bin/activate  # For Windows, use `env\Scripts\activate`
    
### 3. Install dependencies
Install the required packages using `pip`.

    pip install -r requirements.txt

### 4. Run database migrations
    python manage.py migrate

### 5. Create a superuser (optional)
You can create a superuser to access the Django admin interface.

    python manage.py createsuperuser

### 6. Collect static files
    python manage.py collectstatic
    
### 7. Run the development server
    python manage.py runserver
Once the server is running, visit http://127.0.0.1:8000 in your browser to view the application.

### 8. Adding Songs Locally
To play songs locally, add your songs to the /media folder and ensure that they are linked properly in the Django admin or via migrations.

## ⚙️ Technologies Used
- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default)
- Hosting: Vercel (for the live site interface)

## 🔮 Future Plans
In future versions of this project, I am planning to implement the following features:

- Previous/Next Song Buttons: To allow users to skip to the previous or next song in the playlist.
- Song Duration Display: Show the total length of the song and track its progress while playing.
- Seek Bar: A seek bar that users can drag to skip to any part of the song.
- Volume Control: To allow users to adjust the audio volume directly from the player.
- Playlist Support: Enable users to create and manage playlists.
- Loop and Shuffle Features: Allow users to loop a song or shuffle the playlist.

## 🤝 Contributing
This project is open-source, and contributions are highly encouraged! Feel free to add new features, fix bugs, or improve the code.

- Fork the repository.
- Create a new branch for your feature (`git checkout -b feature-branch-name`).
- Commit your changes (`git commit -m 'Add some feature'`).
- Push the branch to your fork (`git push origin feature-branch-name`).
- Open a pull request to the `main` branch of this repository.

> **Note:** Contributions for new features like Previous/Next Song Buttons, Song Duration Display, and other future plans are welcome! You can check out the future plans section for ideas.

## 📝 License
This project is licensed under the MIT License.

## 📧 Contact
If you have any questions or feedback, feel free to reach out to me at: sudhamsingh2412@gmail.com

### Explanation:

- The **"Known Issues"** section highlights the problem with Vercel not serving media files and suggests that users should run the project locally to experience the full functionality.
- The **"Installation"** section provides clear steps on how to install and run the project locally, ensuring they can test the song playback.
- The **"Live Demo"** section links to your hosted site for users to view the interface.
