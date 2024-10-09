// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "drone_msgs/msg/goal.hpp"


using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

class MinimalPublisher : public rclcpp::Node
{
public:
  MinimalPublisher()
  : Node("drone_reg"), count_(0)
  {
    // rclcpp::QoS qos(10);
    // qos.history(rclcpp::HistoryPolicy::KeepLast);
    // qos.durability(rclcpp::DurabilityPolicy::Volatile);
    // qos.reliability(rclcpp::ReliabilityPolicy::BestEffort);
    publisher_ = this->create_publisher<drone_msgs::msg::Goal>("/goal_pose", 10);
    timer_ = this->create_wall_timer(
          1000ms, std::bind(&MinimalPublisher::timer_callback, this));
  }

private:
  int i = 0;
  double points[3] = {1.0,0.0,5.0};
  void timer_callback(){
        auto message = drone_msgs::msg::Goal();
        message.pose.point.x = points[0];
        message.pose.point.y = points[1];
        message.pose.point.z = points[2];
        publisher_->publish(message);
      
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<drone_msgs::msg::Goal>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}
