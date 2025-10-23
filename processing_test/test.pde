void setup() {
  size(400, 400); // 设置窗口大小
}

void draw() {
  background(255); // 白色背景
  fill(255, 0, 0); // 红色填充
  ellipse(mouseX, mouseY, 50, 50); // 随鼠标移动的圆
}