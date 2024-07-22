# Eucalyptus Services : Artist Link Aggregator - Full-Stack Django Application

## Overview

This full-stack web application, built entirely with Django, serves as a comprehensive platform for music artists to showcase their presence across various music platforms and social media. By leveraging Django's powerful backend capabilities and its templating system for the frontend, this project demonstrates an all-in-one solution for web development.

## Key Features

- **Full-Stack Django Implementation**: Utilizes Django for both backend logic and frontend rendering, showcasing the framework's versatility.
- **Artist Management**: Store and manage artist profiles and their associated links.
- **Song/Release Information**: Handle data for individual songs or releases, including links to different streaming platforms.
- **Multi-Platform Link Support**: Display links for various platforms including:
  - Spotify
  - Apple Music
  - SoundCloud
  - YouTube
  - Deezer
  - Social media (Facebook, Instagram, Twitter, etc.)
- **User Authentication**: Secure user authentication system for artists to manage their profiles.
- **Responsive Frontend**: Utilizes Django's templating system to create a responsive and interactive user interface.
- **Database Integration**: Employs PostgreSQL for robust and scalable data storage.

## Technologies Used

- Django (latest version)
- Python 3.x
- PostgreSQL
- HTML/CSS/JavaScript (for frontend enhancements within Django templates)
- Django's built-in authentication system

## Project Structure

- `artist/`: Django app for managing artist-related models, views, and templates
- `song/`: Django app for handling song/release data and related templates
- `users/`: Custom user authentication app
- `templates/`: Directory for shared HTML templates
- `static/`: Static files including CSS, JavaScript, and images
- `eucalyptus_services/`: Main project directory containing settings and top-level URL configurations

## Key Django Features Utilized

- Django ORM for database operations
- Django Forms for data input and validation
- Class-based views for efficient view handling
- Django Template Language for dynamic HTML rendering
- Django's authentication system for user management

## Future Enhancements

- Integration with music streaming APIs for automatic link generation
- Analytics dashboard for artists to track link clicks
- Bulk import/export functionality for artist and song data
- Enhanced search and filtering capabilities
- Mobile app version using Django REST Framework and a mobile frontend framework

## Advantages of the All-in-One Django Approach

- **Rapid Development**: Django's "batteries included" philosophy allowed for quick implementation of both frontend and backend features.
- **Consistency**: Using Django for both layers ensures consistency in data handling and presentation.
- **Simplified Deployment**: The entire application can be deployed as a single unit, simplifying the deployment process.
- **Leveraging Django's Ecosystem**: Ability to easily integrate various Django packages for additional functionality.

## About the Developer

This project was developed by Thibault Paillon to demonstrate proficiency in full-stack web development using Django. It showcases skills in backend logic, database management, frontend design with Django templates, and creating practical solutions for the music industry.

---

Developed with ♥ by Thibault Paillon