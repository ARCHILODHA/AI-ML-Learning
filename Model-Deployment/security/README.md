# API Security

This folder contains basic security guidelines for deployed ML APIs.

## Security Practices

- Validate incoming data
- Limit request size
- Use authentication
- Use HTTPS
- Store secrets in environment variables
- Avoid exposing model files directly
- Implement rate limiting
- Log suspicious requests

## Environment Variables

Sensitive information should never be hardcoded.

Example:

DATABASE_URL=...
API_KEY=...
SECRET_KEY=...

These values should be stored using deployment platform secrets or environment variables.
