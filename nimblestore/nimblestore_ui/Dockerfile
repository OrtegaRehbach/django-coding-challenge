# Stage 1: Build the SvelteKit app
FROM node:20 AS builder

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install --frozen-lockfile

# Copy the rest of the application
COPY . .

# Build the application
RUN npm run build

ENTRYPOINT [ "npm" ]
CMD ["run", "dev", "--", "--host"]

# Stage 2: Run the app in production
FROM node:20-alpine AS runner

# Set working directory
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app/build ./build
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules

# Expose the port the app runs on
EXPOSE 3000

# Command to start the server
ENTRYPOINT ["node"]
CMD ["build"]
