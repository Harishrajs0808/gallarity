## Gallarity – Django-Based Photo Gallery Web App

Gallarity is a modern and responsive photo gallery web application built using Django (Python). It allows users to upload, view, organize, and manage image collections effortlessly through a clean and intuitive web interface.

#Features
*📤 Upload photos with titles, descriptions, and categories
*📁 Organize photos by albums or tags
*🔍 Search and filter images by name or category
*🖼️ Full-screen image previews with lightbox view
*🔐 User authentication (login, logout, signup)
*⚙️ Admin panel to manage gallery and users

#Installation

1. Clone the repository 
git clone https://github.com/yourusername/gallarity.git
cd gallarity

2. Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Create a superuser (optional)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver

Now visit http://127.0.0.1:8000/

# To-Do / Future Enhancements

* Add image comments and likes
* Create public/private gallery mode
* Add user profile pages
* Enable image downloads or sharing
* Integrate cloud storage (AWS S3 or GCP)


#Contributing

We welcome contributions!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/xyz`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/xyz`)
5. Create a Pull Request


#License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


#Acknowledgments

* Django documentation: [https://docs.djangoproject.com](https://docs.djangoproject.com)
* Bootstrap: [https://getbootstrap.com](https://getbootstrap.com)
