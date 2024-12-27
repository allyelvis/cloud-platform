# Sample Dockerfile for Cloud Platform Services
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy application code
COPY . .

# Expose the application port
EXPOSE 8080

# Command to run application
CMD ["node", "index.js"]
