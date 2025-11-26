terraform {
  backend "s3" {
    bucket         = "my-tfstate-prode"
    key            = "infra/terraform.tfstate"
    region         = "us-east-1"
    use_lockfile   = true
    encrypt        = true
  }
}
