#!/usr/bin/env ruby
ARGV[0].scan(/[A-Z]/).each do |i|
  print i
  STDOUT.flush
end
print("\n")
