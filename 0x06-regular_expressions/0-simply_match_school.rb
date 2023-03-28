#!/usr/bin/env ruby
ARGV[0].scan(/School/).each do |i|
  print i
  STDOUT.flush
end
print("\n")
