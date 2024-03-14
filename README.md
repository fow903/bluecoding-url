# Django URL Shortener API Documentation

This document provides information on the available API endpoints for the Django URL Shortener project.

## Shorten URL

Shortens a given URL.

- **URL**: `/shorten/`
- **Method**: `POST`
- **Parameters**:
  - `original_url` (required): The original URL to be shortened.
- **Success Response**:
  - **Code**: `201 CREATED` or `200 OK`
  - **Content**: `{ "shorten_url": "shortened_url", "original_url": "original_url" }`
- **Error Response**:
  - **Code**: `400 BAD REQUEST`
  - **Content**: `{ "message": "original_url is required" }`
  - **Code**: `500 INTERNAL SERVER ERROR`
  - **Content**: `{ "message": "There was an error <error_message>" }`

## Get Original URL

Redirects to the original URL from the shortened URL.

- **URL**: `/redirect/<shortened_url>/`
- **Method**: `GET`
- **Success Response**:
  - **Code**: `301 MOVED PERMANENTLY`
  - **Redirects**: To the original URL
- **Error Response**:
  - **Code**: `404 NOT FOUND`
  - **Content**: `{ "message": "Shorten url does not exist" }`
  - **Code**: `500 INTERNAL SERVER ERROR`
  - **Content**: `{ "message": "There was an error <error_message>" }`

## Get Top Visited URLs

Retrieves the top visited URLs.

- **URL**: `/top-visited/`
- **Method**: `GET`
- **Success Response**:
  - **Code**: `200 OK`
  - **Content**: `{ "top_visited_urls": [ { "original_url": "url", "shorten_url": "shortened_url", "visit_count": count }, ... ] }`
- **Error Response**:
  - **Code**: `500 INTERNAL SERVER ERROR`
  - **Content**: `{ "message": "There was an error <error_message>" }`

## Contributing

Contributions to this project are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
