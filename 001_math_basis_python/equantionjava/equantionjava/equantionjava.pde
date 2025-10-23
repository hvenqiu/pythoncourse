int xmin = -10;
int xmax = 10;
int ymin = -10;
int ymax = 10;
float rangx;
float rangy;
float xscl;
float yscl;

void setup() {
  size(600, 600);
  rangx = xmax - xmin;
  rangy = ymax - ymin;
  xscl = width / rangx;
  yscl = -height / rangy;  // y轴翻转（Processing中向下为正）
}

void grid(float xscl, float yscl) {
  strokeWeight(1);
  stroke(0, 255, 255);  // 青色网格线
  
  // 绘制垂直线
  for (int i = xmin; i <= xmax; i++) {
    line(i * xscl, ymin * yscl, i * xscl, ymax * yscl);
  }
  
  // 绘制水平线
  for (int i = ymin; i <= ymax; i++) {
    line(xmin * xscl, i * yscl, xmax * xscl, i * yscl);
  }
  
  // 绘制坐标轴（黑色）
  stroke(0);
  line(0, ymin * yscl, 0, ymax * yscl);  // y轴
  line(xmin * xscl, 0, xmax * xscl, 0);  // x轴
}

float f(float x) {
  // 原函数：6x³ + 31x² + 3x - 10
  return 6 * x * x * x + 31 * x * x + 3 * x - 10;
}

void graphfunction() {
  stroke(255, 0, 0);  // 红色曲线
  float x = xmin;
  while (x < xmax) {  // 注意原代码中是max，这里修正为xmax
    line(x * xscl, f(x) * yscl, 
         (x + 0.1f) * xscl, f(x + 0.1f) * yscl);
    x += 0.1f;
  }
}

void draw() {
  background(255);  // 白色背景
  translate(width/2, height/2);  // 原点移至中心
  
  // 只绘制一次网格（优化性能）
  grid(xscl, yscl);
  
  graphfunction();  // 绘制函数曲线
}
