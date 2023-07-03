// Command to run project from terminal (replace with path to your folder for sketch=)
// processing-java --sketch="FULL PATH TO SKETCH FOLDER" --run

// Number of points
int n = 25000;

// Init param
float a = 1.97;
float b = -1.50;
float c = 1.98;
float d = -2.50;

// Init x and y
float x_1 = 0;
float x_2 = 0;

void setup(){
  size(1200,700);
}


void draw(){
  // Set background
  background(0);

  // Load in data
  JSONArray values = loadJSONArray("Data/data0.json");

  // Get min and max (for mapping)
  float data_max = 290;
  float data_min = 0;

  // Translate for easier plotting
  translate(width/2, height/2);
  
  // Starting point for ifs
  float x_1 = 0;
  float y_1 = 0;
  
  // Colour points white
  stroke(255);
  
  // Loop for how many points you want to draw
  for (int i = 0; i < n; i++) {
    
    // Update x and y as per De Jong IFS
    x_1 = sin(a*y_1)-cos(b*x_1);
    y_1 = sin(c*x_1)-cos(d*y_1);
    
    // Plot point
    point(x_1*(width/4), y_1*(height/4));
  }

  // Index
  int idx = frameCount % values.size();
  print(idx);
  print("\n");
  
  // Update the value of a
  a = values.getFloat(idx);

  // Map to [-pi,pi]
  a = map(a, data_min, data_max, -PI, PI);
  
}
