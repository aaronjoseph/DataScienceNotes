---
epoch: 1792088701465
mode: agent
backendId: codex
sessionId: "01a135d6-474f-7650-8a24-d304c1280f1a"
agentLabel: "In my notes find all notes pertaining to transformers. I wan…"
usage: '{"usedTokens":360323,"contextWindow":828400,"updatedAt":1792141211798}'
tags:
  - copilot-conversation
---

**user**: In my notes find all notes pertaining to transformers. I want to understand how does it work, then what is BERT and how does transformer, from an architecture perspective is fast? Then in the esci and NER model we have in search 2.0 architecture, can you map how does it work also with the dense model in recall? I need a learning plan first, so create a document with checklist of things I need to read up on, additionally, structure the same in terms of notes 

Like 

link

followed by what is the essential content to understand here?

Link 
content


Name this understanding transformer to Search 2.0?

I need detailed info on how does NER, ESCI and sparse model here works? detail it out for me
[Timestamp: 2026/10/15 23:55:01]

**ai**: I’ll find your transformer-related notes, read the Search 2.0 architecture, and build a linked learning plan covering the fundamentals and how NER, ESCI, dense recall, and sparse recall fit together.I’m using the Obsidian Markdown and Copilot web-search skills. I’ll distinguish the model concepts from what your architecture note actually documents, especially where checkpoint names, training details, or serving behavior still need confirmation.Your vault already has the main building blocks: Transformers, BERT, NER, dense retrieval, SPLADE, cross-encoders, and ESCI. The key gap is connecting them into one learning sequence.

The Search 2.0 note records a September 26 source snapshot. It documents calls to NER, dense/sparse embedding, and ESCI services, but does not establish their internal checkpoints or training recipes. I’ll explain the standard architectures in detail and mark what remains unknown about your models.The draft learning plan is written, with a checklist and essential reading points under each note link. It also includes detailed NER, dense-recall, sparse/SPLADE, and ESCI walkthroughs tied to one example query.

I found two existing claims worth correcting in the plan: LSTMs can run on GPUs, and Transformers do not have infinite context. The plan also separates remote ESCI inference from the local ONNX ranker, since they play different roles in the documented flow.The plan inventories 48 relevant notes and separates out two scikit-learn terminology matches. It has 46 checklist items, detailed model explanations, and an end-to-end Search 2.0 diagram.

The document also records that the architecture snapshot selects `text-embedding-005` for dense recall; it does not assume BERT is that model’s backbone. Link, heading, YAML, footnote, and worked-example checks have passed. I’m checking whether an Obsidian reading-view preview is available.Created [[outputs/Understanding Transformer to Search 2.0|Understanding Transformer to Search 2.0]].

It includes:

- **48 relevant notes**, with links and essential reading points.
- **Seven learning sessions and 46 checklist items**.
- Detailed explanations of Transformers, BERT, architectural speed, NER, dense recall, sparse/SPLADE recall, and ESCI.
- An end-to-end Search 2.0 diagram and worked examples.
- Explicit gaps separating documented behavior from unverified model internals.

Links, headings, YAML, footnotes, and calculations passed checks. Obsidian rendering remains unverified because its CLI was unavailable.


[Timestamp: 2026/10/15 23:55:01]

**user**: Is this added to the action plan document?
[Timestamp: 2026/10/16 00:13:05]

**ai**: I’ll check whether the new learning plan is linked from [[Action-Plan]] and included in [[Action Plan.base]].Not yet. [[Action-Plan]] has general Transformer/BERT readings, but no link to [[outputs/Understanding Transformer to Search 2.0|Understanding Transformer to Search 2.0]] or its checklist.

The new note matches [[Action Plan.base]]’s general `search-eng` filter, so it should appear in **All search notes**, but it hasn’t been added to the curated reading views.
[Timestamp: 2026/10/16 00:13:05]

**user**: refer to this file - /Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/AGENTS.md

In the current file, when we are going with high level, can we detail out in Search 2.0 architecture, the math behind it? The math doesnt' seem very clear on recall, rrf and relevant link and how does dense and sparse work? I need help with that as well please let me know if you can refer to the agent file in this location - /Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/AGENTS.md

Help with the details please
[Timestamp: 2026/10/16 11:05:13]

**ai**: I’ll read the serving-rs agent instructions and trace the current recall implementation, then expand [[Search2.0 architecture]] with the dense/sparse scoring math, worked examples, and links to the relevant notes. I’ll verify where RRF actually applies so the explanation matches the code.I can access that AGENTS.md file. I’m using the readrust and Obsidian Markdown skills to follow its source-navigation guidance and preserve the note’s structure. The serving repository will be read-only; the changes will stay in the vault note.The current code makes an important distinction: recall sends separate dense-only and sparse-only tier requests. Sparse requests carry an RRF block with alpha `0`; dense requests omit it. The service then merges tier results in plan order—it does not run a global RRF calculation over all returned tiers.

I also found that the note’s September snapshot has older recall budgets and fan-out rules. I’ll update that section to the inspected revision, with worked math that clearly separates general RRF from the current serving path.The expanded section now has step-by-step dense, sparse, and RRF calculations, plus a filter/top-K explanation and a current fan-out example: under the stated two-type assumptions, recall plans 13 requests with 900 neighbor slots.

It also explains the current ESCI/type-selection rules. In this revision, SKU retention is Exact/Substitute only; the older `explicit_attribute` exception is gone. I’ve dated the refreshed sections so the rest of the note’s September snapshot isn’t mistaken for a full current audit.The link, heading, metadata, footnote, and example-arithmetic checks passed. Existing headings and embeds are preserved, and the serving repository is unchanged.

The updated text is visible to Obsidian, but I couldn’t reliably verify its reading-view rendering. The note also keeps the remaining gaps explicit: the deployed index metric and the private model services’ exact internals still need verification.Yes—I read the requested serving-rs AGENTS.md and updated [[Search2.0 architecture#Read the Recall Mathematics in This Order|Search2.0 architecture]].

Added detailed explanations and worked calculations for:

- Dense vectors, dot products, cosine similarity, and distances.
- Sparse weights and SPLADE-style expansion.
- Filters, top-K, per-type fan-out, and candidate budgets.
- RRF, ordered merging, and deduplication.
- ESCI retention and type-level relevance.

**Key finding:** the inspected code uses separate dense/sparse requests and ordered merging; it does not globally RRF-fuse all tiers.

The refreshed sections identify their source revision. Links and example arithmetic passed checks; rendered layout remains unverified.


[Timestamp: 2026/10/16 11:05:13]

**user**: remove all date related history, I want it as a clean detail of the implementation without such details

**Source snapshot:** inspected on **26 September 2026**, repository `/Users/A3126435/Desktop/Projects/aml-ai-search`, branch **`pre-prod`**, commit **`1dfaa528621e7306135ffc62a0972508091cd4f9`**. The source checkout was clean at inspection. Paths below beginning with `crates/`, `knowledge/`, or `deploy/` are relative to its `serving-rs/` directory; the reference section links to that exact source revision.

**Scoped recall/math refresh — 16 October 2026:** the recall section and its relevance bridge were checked against local branch **`rs_deployment`**, commit **`dbd5369fd410b73579758774645d65eba192a2ad`**, with a clean source checkout. The requested `serving-rs/AGENTS.md`, `knowledge/index.md`, `knowledge/README.md`, relevant walkthroughs, and executable recall/transport/type-filter code were read. These refreshed sections use new references marked `recall-current` or `recall-math`. **Other sections retain the 26 September snapshot unless explicitly marked otherwise**; in particular, older session-cache, LTR, ESCI-cache, startup, and deployment descriptions need a separate refresh before treating them as current behavior. This pass adds explanations and corrects the inspected recall boundary; it does not certify a deployment.
[Timestamp: 2026/10/16 13:55:08]

**ai**: I’ll remove the dated review history from [[Search2.0 architecture]] and rewrite those passages as direct implementation descriptions. I’ll also check for historical qualifiers elsewhere in the note so the cleanup is consistent.Updated [[Search2.0 architecture]] to remove dated snapshots, review logs, and historical update commentary throughout.

It now reads as a direct implementation explanation, preserving the math, examples, diagrams, references, and open questions. Links and document structure passed checks.
[Timestamp: 2026/10/16 13:55:08]

**user**: Would you have access to the code repo? If so can you validate what exactly is TLS thats attached to the redis?
[Timestamp: 2026/10/16 13:58:32]

**ai**: Yes, I can read the code repository. I’ll trace the Redis connection setup and explain exactly what TLS does there, including which certificates and checks the code uses.The code uses Redis over TLS on port `6378`, with a custom CA certificate loaded from Secret Manager. The Redis password is separate from that certificate. I’m checking the client-library behavior to confirm how server verification works and whether the connection uses client certificates.Yes—I have read access to the repository and traced the Redis connection code.

**TLS means Transport Layer Security. Here, it protects the network connection between your Rust service and Redis.** The same underlying protocol protects HTTPS connections, but this connection carries Redis commands rather than HTTP.

```text
Rust service ── encrypted TLS connection ── Redis
                       port 6378
```

For example, when recall reads an embedding from Redis, TLS protects the command, key, returned vector, and authentication traffic while they travel across the network.

Your implementation configures three separate pieces:

| Piece | What it does |
|---|---|
| `rediss://` connection | Enables Redis over TLS |
| CA certificate in PEM format | Establishes which certificate authority the client trusts when checking Redis’s server certificate |
| Redis password | Authenticates the application to Redis |

At startup, the application loads the **password and CA certificate separately from Google Secret Manager**. See [state.rs:393](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/api/src/state.rs:393).

The connection setup then contains:

```rust
let certificates = redis::TlsCertificates {
    client_tls: None,
    root_cert: Some(ca_pem),
};
```

This means:

- **`root_cert: Some(ca_pem)`** supplies the trusted CA certificate. It is trust material—not the secret key used to encrypt every command.
- **`client_tls: None`** means the application does **not** present a client certificate: this setup is **not mutual TLS (mTLS)**.
- The application uses a Redis password alongside TLS, and its connection builder does not request an insecure verification bypass. See [redis_support.rs:328](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/infra/src/redis_support.rs:328). The [Redis library documentation](https://docs.rs/redis/latest/redis/struct.TlsCertificates.html) explains these certificate fields.

Conceptually, connection establishment is: connect → perform TLS handshake and validate the server certificate → establish encryption keys → authenticate to Redis → exchange commands over the protected connection. Existing pooled connections are reused; every cache lookup does not require a new handshake.

**What I verified is the client implementation.** I have not connected to Redis or retrieved the certificate secret, so its actual issuer, expiry, and the negotiated TLS version remain unverified. TLS also protects data **in transit**; it does not establish whether Redis data is encrypted at rest.


[Timestamp: 2026/10/16 13:58:32]

**user**: Also can you validate, in product Search code, when you validate query and count what does count mean here?

And resolve customer location what does that mean

What is the redis call that happens in product search before we hit NER?
[Timestamp: 2026/10/16 14:04:38]

**ai**: I’ll trace those three steps in the current product-search code: the count validation, customer-location resolution, and any Redis calls before NER.“Count” means the requested result count (`num_results`), which the domain calls `limit`; it is not a word or token count.

I also found a mismatch in the architecture note: the current Rust NER cache is in process and keyed by the rewritten query, not a Redis session lookup. Redis calls before NER can instead come from location resolution, query-rewrite refresh, or the more-like-this path. I’m checking those conditions so I can distinguish what runs on every request from what is optional.Yes—I checked the current Rust product-search path. These steps mean:

1. **“Validate query and count” checks the search text and requested result count.**

   The API field is `num_results`; the handler maps it to the domain field `limit`.

   ```json
   {
     "query": "gaming laptop",
     "num_results": 20
   }
   ```

   The checks reject:
   - A blank or whitespace-only query.
   - A count of zero.
   - A count greater than 1,000.

   Omitted `num_results` defaults to **100**. This count is **not the number of query words, tokens, or vector neighbors**. See [request mapping](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/api/src/handlers/product_search.rs:41) and [validation](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/service.rs:179).

   **Important:** the requested count is not consistently enforced as a final response limit. Recall uses its own tier budgets; the normal reranker separately caps results at **100 parent products, with up to five SKUs each**. Therefore, requesting 20 does not currently guarantee at most 20 returned products.

2. **“Resolve customer location” translates supplied location information into fulfillment-location IDs.**

   It answers: **“Which stores or fulfillment locations should this search consider?”**

   It does not detect the customer’s location automatically or check product inventory yet.

   For example, a supplied ZIP code can resolve to an illustrative map:

   ```json
   {
     "instore": ["store-A", "store-B"],
     "shipping": ["warehouse-C"]
   }
   ```

   The implementation:
   - Looks up a supplied ZIP code in Redis.
   - Otherwise uses the caller’s `location_id_map`.
   - Expands preferred stores to include nearby stores and replaces the `instore` group.
   - Applies allowed fulfillment channels and selection-specific rules that can clear the map.

   Recall and ranking subsequently use this context for availability-related retrieval and inventory checks. See [location resolution](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/location.rs:36).

3. **There is no Redis NER-session lookup in the current Rust path.**

   The architecture note’s description of reading cached NER by `search_id` is inaccurate for this implementation.

   These Redis operations can happen **before NER**, depending on the request and configuration:

   | Condition | Redis command | Purpose |
   |---|---|---|
   | ZIP code supplied | `GET ZIP:<zipcode>` | Resolve fulfillment-location groups |
   | Preferred stores supplied | Pipelined `GET LOCATION:<store_id>` | Find nearby stores |
   | More-like-this enabled | `HMGET SKU:<sku> ...` | Load the anchor product’s metadata |
   | Redis query rewriting enabled and refresh due | `GET <rewrite-map-key>` | Refresh query rewrites; default key is `ACTIVE_QUERY_REWRITES` |

   The rewrite map normally serves from memory; its refresh interval is five minutes. Active types, model families, and features also use in-memory snapshots maintained by background refreshes.

   **NER itself uses an in-process cache keyed by the exact rewritten query.** A hit reuses the entities; a miss calls the NER HTTP service. The default cache holds up to 10,000 successful responses for 14 hours. `search_id` and `query_id` are correlation fields, not cache keys. See [the pre-NER sequence](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/service.rs:334), [Redis location commands](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/infra/src/location/redis.rs:115), and [NER caching](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/infra/src/ner/caching.rs:1).

These are source-verified behaviors; I haven’t traced a live request.
[Timestamp: 2026/10/16 14:04:38]

**user**: Referring to this redis in produc_search.api with redis.get can we understand what that does


Key
Value
busy_ns	97392
code.file.path	crates/infra/src/location/redis.rs
code.line.number	98
code.module.name	serving_infra::location::redis
db_operation	GET
db_system	redis
gcp.project_id	bbyus-srv-aml-ai-search-p04
idle_ns	528160
key_prefix	ZIP:
service.name	rs-product-search
target	serving_infra::location::redis
thread.id	4
thread.name	tokio-rt-worker
zipcode	98004

<!-- copilot-image:e4908760fe90d3076ed2e078500cb3d4c5e65b7a26663be70da42b9b394f13b9 -->
![[copilot-image-e4908760fe90d3076ed2e078500cb3d4c5e65b7a26663be70da42b9b394f13b9.png]]
<!-- /copilot-image -->
[Timestamp: 2026/10/16 14:10:08]

**ai**: I’ll match this span to the ZIP lookup code and separate what its timing tells us from what would require the Redis response or additional logs.Yes—**this span is the ZIP-code-to-fulfillment-locations lookup**. Given `key_prefix=ZIP:` and `zipcode=98004`, the code constructs and executes:

```redis
GET ZIP:98004
```

The exact call is in [redis.rs:109](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/infra/src/location/redis.rs:109). Line **98** in your trace points to the instrumentation annotation that creates the `redis.get` span.

It answers: **“Which stores or fulfillment locations serve this ZIP code?”**

The expected Redis value is a JSON object mapping availability channels to location IDs. For example—illustrative, not the actual stored value:

```json
{
  "instore": ["store-A", "store-B"],
  "shipping": ["warehouse-C"],
  "same_day_shipping": ["location-D"]
}
```

The function reads that string, parses the JSON, and returns the location map. Product search then applies preferred-store and fulfillment-selection rules. Recall and ranking use the resulting context for availability-related retrieval and checks. **This call does not retrieve products, check an individual product’s stock, or fetch NER entities.**

Your timings mean:

| Attribute | Converted value | Interpretation |
|---|---:|---|
| `busy_ns=97392` | 97.392 μs | Time the tracing span was entered |
| `idle_ns=528160` | 528.160 μs | Time it existed without being entered |
| Combined | **625.552 μs ≈ 0.626 ms** | Approximately the function’s elapsed duration |

“Busy” is **not a precise CPU measurement**, and “idle” is **not exclusively Redis server time**. With async code, the latter can include waiting for I/O and scheduling. These definitions come from [tracing-opentelemetry’s inactivity tracking](https://docs.rs/tracing-opentelemetry/latest/tracing_opentelemetry/struct.OpenTelemetryLayer.html#method.with_tracked_inactivity). The span covers the whole function, including parsing—not just Redis execution.

The attributes alone **do not establish whether the key existed or what locations it returned**. The code returns an empty map on a missing key, Redis error, or unusable JSON. Corresponding events are:

- `location.zipcode_not_found`
- `location.zipcode_lookup_failed`
- `location.zipcode_decode_failed`

This explains why the span appears before NER: customer-location resolution happens first and is independent of understanding the query text.
[Timestamp: 2026/10/16 14:10:08]

**user**: explain more about MLT or more like this and tell me the load anchor metadata, and seed filter where is this table and a sample query that can trigger that? what is the need for this in Search
[Timestamp: 2026/10/16 14:13:30]

**ai**: I’ll trace the more-like-this branch, identify where the anchor product’s metadata is stored, and give you a sample request that triggers it. I’ll also explain how its filters differ from an ordinary text search.**More Like This (MLT) means “find alternatives to this product.”** Instead of starting with the customer’s description, search starts with an existing product—the **anchor**—and uses its name, product type, and price to construct a search.

For example: a customer is viewing wireless headphones priced at 200 and selects “similar products.” That product becomes the anchor.

**1. What “load anchor metadata” does**

The anchor is identified by its **SKU**. The implementation reads a Redis **hash**, rather than querying a SQL table:

```redis
HMGET SKU:<anchor_sku> name_short product_type_id current_price conditions
```

It uses the **product-search Redis pool**. The fields are:

| Field | Purpose |
|---|---|
| `name_short` | Becomes the text query used to find alternatives |
| `product_type_id` | Seeds the product-type restriction |
| `current_price` | Seeds a nearby-price range |
| `conditions` | Loaded into metadata; the seed-filter function does not directly add a condition filter from it |

The exact lookup is in [Redis MLT metadata](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/infra/src/mlt/redis.rs:82).

For an **illustrative** anchor `1234567`, Redis might contain:

```text
Key: SKU:1234567

name_short       Sony wireless over-ear headphones
product_type_id  headphones
current_price    200
conditions       new
```

These are invented values, not a verified Redis record. The serving code establishes where it reads them; I haven’t traced the upstream job that populates that hash.

**2. What “seed filters” means**

“Seed” means **initialize the search constraints from the anchor’s attributes**. There is no separate “seed-filter table”: the code creates these filters in memory.

For the example above, it creates:

```text
product_type_id = headphones
current_price >= 100
current_price <= 300
```

The configured price variation is **±50%**.

With anchor price 200:

**Lower bound:**

$$
200 \times (1-0.5)=100
$$

**Upper bound:**

$$
200 \times (1+0.5)=300
$$

The intent is to find comparable products in the same type and a reasonably similar price band. A missing or zero anchor price produces no anchor-price range.

See [seed-filter construction](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/more_like_this.rs:29).

**3. What the complete search does**

The MLT branch:

1. Treats the incoming `query` as an anchor SKU.
2. Reads its Redis metadata.
3. Sets `in_stock=true`.
4. Replaces the effective query with the anchor’s `name_short`.
5. Sets the internal prompt marker to `more_like_this`.
6. Continues through query rewriting, NER, recall, and reranking.
7. Replaces the NER-derived product-type restriction with the anchor’s type and adds the anchor-price range.

It retains only the permitted MLT filter names: `product_type_id`, `brand`, `current_price`, `conditions`, and `order_code`. Consequently, it does not blindly carry every attribute inferred from the anchor title into retrieval.

One implementation detail: ordinary brand filters use `co_brands`, which is outside that whitelist, so **MLT does not automatically require the same brand**.

The flow starts in [product-search preprocessing](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/service.rs:262); filter replacement is implemented in [apply_mlt_filters](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/more_like_this.rs:67).

**4. A request that triggers it**

Send a POST to `/api/v1.0/predictions`:

```json
{
  "search_id": "mlt-example-search",
  "query_id": "mlt-example-query",
  "query": "REPLACE_WITH_EXISTING_SKU_ID",
  "enable_more_like_this": true,
  "num_results": 20,
  "zip_code": "98004"
}
```

Replace the placeholder with a real SKU whose `SKU:<id>` hash has a nonempty `name_short`. The ZIP code is optional and supplies customer fulfillment context.

**The flag triggers MLT—not the phrase “more like this” in the query.** If the anchor metadata is missing or its name is empty, the code returns an `INVALID` result rather than searching for the SKU string.

**5. Why search needs this**

It supports product-discovery flows such as:

- Finding alternatives to an unavailable product.
- Comparing similar products while browsing a product page.
- Discovering other brands or nearby price options without writing a new query.

The existing search pipeline provides the semantic retrieval, relevance classification, availability handling, and ranking. MLT supplies a product-derived starting point.

Two limits matter: the anchor-removal helpers stop after the first matching parent, and an empty-result broadened retry can **drop the price range**. The initial ±50% band therefore isn’t an unconditional constraint on every fallback response. See [fallback policy](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/recall_handoff.rs:268).
[Timestamp: 2026/10/16 14:13:30]

**user**: can you explain the following, how does MLT get triggered or is it a generic search flow
[Timestamp: 2026/10/16 14:20:45]

**ai**: **MLT is an explicitly triggered branch of the same product-search API.** A normal search does not automatically become MLT.

The request flag determines the behavior:

| Request | Meaning of `query` | Behavior |
|---|---|---|
| `enable_more_like_this` omitted or `false` | Search text | Ordinary product search |
| `enable_more_like_this: true` | Existing product’s SKU | More-like-this search |

**Ordinary search:**

```json
{
  "search_id": "search-1",
  "query_id": "query-1",
  "query": "wireless headphones under 200"
}
```

The service interprets the text, builds filters, retrieves candidates, and ranks them.

**MLT search:**

```json
{
  "search_id": "search-2",
  "query_id": "query-2",
  "query": "EXISTING_SKU_ID",
  "enable_more_like_this": true
}
```

The service first loads that SKU’s metadata, then converts it into a search:

```text
Anchor SKU
    ↓
Load product name, type, and price from Redis
    ↓
Use product name as the effective text query
Seed anchor-type and nearby-price filters
    ↓
Continue through NER → recall → reranking
```

The branch is controlled by `if request.more_like_this` in [product-search code](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/service.rs:262).

A “Find similar products” button could send this flag and the viewed product’s SKU. **The backend code confirms the trigger contract; I haven’t verified which frontend currently sends it.**

Typing “more like this” or supplying a SKU alone does not activate MLT. Without the flag, a SKU may instead follow the separate direct-product-lookup path.
[Timestamp: 2026/10/16 14:20:45]

**user**: is it driven by sku id, if I pass sku id it works?
[Timestamp: 2026/10/16 14:23:12]

**ai**: Yes—**MLT is driven by a SKU ID, but you must also enable the MLT flag**:

```json
{
  "search_id": "search-1",
  "query_id": "query-1",
  "query": "YOUR_EXISTING_SKU_ID",
  "enable_more_like_this": true
}
```

For it to proceed, Redis must contain `SKU:YOUR_EXISTING_SKU_ID` with a nonempty `name_short`. The service uses that name to search for alternatives, with available anchor-type and price constraints.

**Passing only a SKU ID does not trigger MLT.** Without the flag, it follows ordinary search or direct-lookup handling.
[Timestamp: 2026/10/16 14:23:12]

**user**: I have the the following file in downloads, can you help me understand the flow of this MLT flow?
[Timestamp: 2026/10/16 14:28:21]

**ai**: I don’t see a filename or attachment in your message. I’ll check the recent filenames in Downloads to help identify it.The newest file is `downloaded-logs-20261016-142510.json`. I’ll inspect it for MLT events, assuming that’s the file you mean.This file does contain an MLT request for SKU `5902426`, resolved to `Apple - HomePod mini 2 - Midnight`. The first retrieval pass produced candidates, but ESCI classified all 28 SKUs as Irrelevant. Search then retried without the price filters and returned one product.

I’ll walk through both passes and keep the parent-product and SKU counts separate.I inspected the newest file, [downloaded-logs-20261016-142510.json](/Users/A3126435/Downloads/downloaded-logs-20261016-142510.json), assuming that is the one you meant.

**This request successfully entered MLT, but its first search returned no acceptable matches. A second search removed the price restriction and ultimately returned one product.**

```text
Anchor SKU: 5902426
    ↓
Resolve title: Apple - HomePod mini 2 - Midnight
    ↓
Search within anchor type and nearby price range
    ↓
28 candidate SKUs → ESCI marks all Irrelevant
    ↓
Retry without price filters
    ↓
52 candidate SKUs → 2 Substitute SKUs survive
    ↓
Final ranking/grouping → 1 product
```

**1. The request explicitly triggers MLT**

The initial logs contain:

```text
search_query = "5902426"
more_like_this = true
limit = 100
```

Therefore, `5902426` is interpreted as the **anchor SKU**, rather than ordinary search text.

The incoming request has `in_stock=false`, but MLT subsequently forces it to `true`. The initial log occurs before that override.

**2. The anchor metadata resolves successfully**

The log records:

```text
stage = "mlt_metadata"
outcome = "ok"
```

The subsequent effective query is:

```text
Apple - HomePod mini 2 - Midnight
```

That shows the anchor was resolved and its product name became the search text. The query-rewrite stage reports `rewritten=false`: the rewrite map did not change this title.

The corresponding code reads:

```redis
HMGET SKU:5902426 name_short product_type_id current_price conditions
```

The raw Redis response is not included in the export. See [anchor lookup code](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/infra/src/mlt/redis.rs:82).

**3. MLT creates the initial search constraints**

The logged filters are:

```text
order_code IN [buy, pre-order, instore]
product_type_id = Voice_Activated_Assistants
current_price >= 74.995
current_price <= 224.985
```

The type comes from the anchor metadata. The price bounds are consistent with an **anchor price of 149.99**, using the implementation’s ±50% rule. That price is inferred from the bounds; it is not directly logged as anchor metadata.

The retrieval boundary normalizes the type to:

```text
voice_activated_assistants
```

**4. NER runs on the product title**

The NER cache reports a miss, so the service calls NER. Extraction takes approximately **34 ms**.

An important distinction in these logs:

```text
ner_type_group_count = 4
ner_present = false
query_intent = MORE_LIKE_THIS
```

`ner_present=false` does **not** mean NER failed or returned no entities. The MLT intent branch returns default intent metadata, which includes this false flag. See [intent classification](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/intent.rs:122).

**5. The first recall pass executes five dense tiers**

Both dense and sparse embeddings are obtained, but **all five actual vector-search requests are dense-only**, with `rrf_present=false`.

| Tier | First-pass neighbor rows |
|---|---:|
| Excluded-condition dense | 1 |
| Available in-store | 13 |
| Available shipping | 18 |
| Available delivery | 0 |
| Available digital | 0 |
| **Total** | **32** |

The ordinary NER-gated tiers are skipped because `ner_present=false`. Broad unfiltered tiers are suppressed by the MLT prompt marker. Condition and availability tiers still run.

After deduplication and Spanner expansion, recall produces **18 parent products containing 28 SKUs**. The different counts represent different stages and units.

**6. ESCI removes every first-pass candidate**

Metadata is available for all 28 SKUs, and none has empty ESCI input text. The ESCI cache misses, so all 28 are submitted to the model.

The result is:

```text
Irrelevant: 28
Exact:       0
Substitute:  0
```

The Exact/Substitute retention rule therefore leaves **zero SKUs**.

This is a successful inference path with no accepted matches—not evidence of an ESCI timeout or missing product text. The export does not establish *why* the model classified every candidate as Irrelevant.

**7. Search retries with broader constraints**

The logs then show:

```text
product_search.graceful_fallback.started
retry_enabled = true
```

The second recall request keeps the product type and order-code restrictions but changes:

```text
numeric_filter_count: 2 → 0
```

**The price band is removed.** The query title stays unchanged. This follows the [MLT fallback policy](/Users/A3126435/Desktop/Projects/aml-ai-search/serving-rs/crates/domain/src/product_search/recall_handoff.rs:268).

**8. The fallback produces the final result**

| Boundary | Initial pass | Fallback |
|---|---:|---:|
| Raw neighbor rows | 32 | 65 |
| Recalled parent products | 18 | 38 |
| Candidate SKUs | 28 | 52 |
| ESCI Irrelevant | 28 | 50 |
| ESCI Substitute | 0 | 2 |
| Final products | 0 | 1 |

The two surviving SKU IDs are `6519336` and `6519349`. They proceed through availability and the ONNX LTR ranking branch; final ranking/grouping emits **one product**.

The completed request reports:

```text
model_status = 217
model_status_info = MORE_LIKE_THIS
is_graceful_fallback = true
product_count = 1
duration_ms = 889
```

**The practical implication:** this request returned one MLT product through fallback, and that result was no longer constrained by the original ±50% price band. The export does not contain enough final product detail to identify its displayed title or price.
[Timestamp: 2026/10/16 14:28:21]