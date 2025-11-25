FROM openjdk:17-jdk-slim
WORKDIR /app
COPY public /app/public
COPY src /app/src
RUN mkdir -p /app/out \
 && javac -d /app/out /app/src/com/vivo/ctf/*.java
ENV FLAG="CTF{java_insecure_deserialize}"
EXPOSE 8080
CMD ["sh", "-c", "echo -n \"$FLAG\" > /flag || true; java -cp /app/out com.vivo.ctf.JobServer"]
