# Use the official Node.js image.
FROM node:14

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Expose the port that your app runs on
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]
