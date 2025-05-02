provider "aws" {
  region = "us-west-2"  # or your preferred region
}

resource "aws_key_pair" "deployer" {
  key_name   = "pubmedqa-key"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_security_group" "pubmedqa_sg" {
  name        = "pubmedqa-sg"
  description = "Allow SSH and HTTP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "pubmedqa_instance" {
  ami           = "ami-0fc5d935ebf8bc3bc"  # Ubuntu 20.04 LTS (free-tier eligible, us-west-2)
  instance_type = "t2.micro"
  key_name      = aws_key_pair.deployer.key_name
  security_groups = [aws_security_group.pubmedqa_sg.name]

  tags = {
    Name = "pubmedqa-ec2"
  }

  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }

    inline = [
      "sudo apt-get update -y",
      "sudo apt-get install -y docker.io git",
      "sudo usermod -aG docker ubuntu",
      "git clone https://github.com/<your-github>/pubmedqa-lite.git",
      "cd pubmedqa-lite && sudo docker build -t pubmedqa .",
      "sudo docker run -d -p 80:8000 pubmedqa"
    ]
  }
}
