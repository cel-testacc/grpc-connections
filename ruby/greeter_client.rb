this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'lib')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'helloworld_services_pb'

def main
  user = ARGV.size > 0 ? ARGV[0] : 'cworld'
  hostname = ARGV.size > 1 ? ARGV[1] : 'localhost:50051'
  stub = Helloworld::Greeter::Stub.new(hostname, :this_channel_is_insecure)
  begin
    message = stub.say_hello(Helloworld::HelloRequest.new(name: user)).message
    p "Greeting: #{message}"
  rescue GRPC::BadStatus => e
    abort "ERROR: #{e.message}"
  end
end

main
