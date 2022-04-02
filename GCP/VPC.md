- Each VPC network is contained in a GCP project
- You can provision Cloud Platform resources, connect them to each other, and isolate them from one another
- VPC have routing tables, that allow it to forward traffic between one instance to another within the same network, even across subnetworks and even between GCP zones
- VPC provides global distributed firewalls, which dictates which traffic is allowed
- Use `VPC peering` to interconnect networks in GCP projects

Global HTTP(S) | Global SSL Proxy | Global TCP Proxy | Regional | Regional Internal
--|--|--|--|--
Layer 7 load balancing based on load | Layer 4 load balancing of non-HTTPS SSL Traffic based on load |Layer 4 load balancing of non-SSL TCP traffic| Load balancing of any traffic | Load balancing of traffic inside a VPC
Can route different URLS to different back ends | Supported on specific port numbers | Supported on specific port numbers | Supported on any port number | Use for the internal tiers of multi-tier applications