FROM golang:latest

RUN mkdir /build
WORKDIR /build
COPY . /build

RUN go build main.go


FROM alpine:latest

COPY --from=0 /build/main .
CMD ["./main"]
