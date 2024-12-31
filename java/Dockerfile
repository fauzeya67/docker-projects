#Base Image
FROM openjdk:17-jdk-alpine
#working directory
WORKDIR /app
##copy code
COPY src/Main.java /app/Main.java
##compile code
RUN javac Main.java
##run
CMD ["java", "Main"]
