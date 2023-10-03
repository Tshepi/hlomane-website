terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 3.27"
    }
  }
}

provider "aws" {
  profile = "default"
  region = "eu-west-1"
}

resource "aws_s3_bucket" "hlomane" {
    bucket = "hlomane-bucket"
    tags = {
      Name = "hlomane-website-1"
      Environment = "Development"
    }
}

resource "aws_s3_bucket_website_configuration" "hlomane-website" {
  bucket = aws_s3_bucket.hlomane.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}