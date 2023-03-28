#!/usr/bin/env ruby
ARGV[0].scan(/^hbt{2,5}n$/).each do |i|
  print i
  STDOUT.flush
end
print("\n")
