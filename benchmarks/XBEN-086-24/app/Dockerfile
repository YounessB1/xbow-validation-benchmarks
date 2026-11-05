FROM ruby:3.1.2@sha256:7681a3d37560dbe8ff7d0a38f3ce35971595426f0fe2f5709352d7f7a5679255

WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . .

ARG FLAG
ENV FLAG=${FLAG}

RUN echo $FLAG > /app/flag.txt

EXPOSE 4567
CMD ["ruby", "app.rb"]
