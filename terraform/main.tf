resource "aws_ecs_cluster" "main" {
  name = "simple-time-service-cluster"
}

resource "aws_ecs_task_definition" "main" {
  family                   = "simple-time-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.ecs_task_execution.arn
  container_definitions = jsonencode([{
    name      = "simple-time-container"
    image     = "jaisankar07/simple-time-service:latest"
    portMappings = [{
      containerPort = 5000
      hostPort      = 5000
    }]
  }])
}

resource "aws_ecs_service" "main" {
  name            = "simple-time-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.main.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    subnets         = aws_subnet.public[*].id
    assign_public_ip = true
    security_groups  = [aws_security_group.alb_sg.id]
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.main.arn
    container_name   = "simple-time-container"
    container_port   = 5000
  }

  depends_on = [aws_lb_listener.main]
}