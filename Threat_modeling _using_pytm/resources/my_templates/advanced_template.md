<link href="docs/Stylesheet.css" rel="stylesheet"></link>

## pytm - A Python Framework for Threat Modeling
Some part of the original source code is customized by Jahidul Arafat to added intended functionalities and threats

---

**New Additions** <br>
- Oracle Cloud Infrastructure (OCI) Serverless Function is added<br>
- OCI Object Storage buckets, OCI VCN is added<br>
- Report Generation Template files are customized<br>

---

## System Description

{tm.description}

## Dataflow Diagram - Level 0 DFD

![](../../project-2-threat_modeling-jurassic-park/outputs/dfd.png)

&nbsp;

## Dataflows

Name|From|To |Data|Protocol|Port
|:----:|:----:|:---:|:----:|:--------:|:----:|
{dataflows:repeat:|{{item.display_name:call:}}|{{item.source.name}}|{{item.sink.name}}|{{item.data}}|{{item.protocol}}|{{item.dstPort}}|
}

## Data Dictionary

Name|Description|Classification|Carried|Processed
|:----:|:--------:|:----:|:----|:----|
{data:repeat:|{{item.name}}|{{item.description}}|{{item.classification.name}}|{{item.carriedBy:repeat:{{{{item.name}}}}<br>}}|{{item.processedBy:repeat:{{{{item.name}}}}<br>}}|
}

## Actors

{actors:repeat:
Name|{{item.name}}
|:----|:----|
Description|{{item.description}}|
Is Admin|{{item.isAdmin}}
Finding Count|{{item:call:getFindingCount}}|

{{item.findings:if:

**Threats**

{{item.findings:repeat:
<details>
  <summary>   {{{{item.id}}}}  --  {{{{item.threat_id}}}}   --   {{{{item.description}}}}</summary>
  <h6> Targeted Element </h6>
  <p> {{{{item.target}}}} </p>
  <h6> Severity </h6>
  <p>{{{{item.severity}}}}</p>
  <h6>Example Instances</h6>
  <p>{{{{item.example}}}}</p>
  <h6>Mitigations</h6>
  <p>{{{{item.mitigations}}}}</p>
  <h6>References</h6>
  <p>{{{{item.references}}}}</p>
  &emsp;
</details>
}}
}}
}

## Boundaries 

{boundaries:repeat:
Name|{{item.name}}
|:----|:----|
Description|{{item.description}}|
In Scope|{{item.inScope}}|
Immediate Parent|{{item.parents:if:{{item:call:getParentName}}}}{{item.parents:not:N/A, primary boundary}}|
All Parents|{{item.parents:call:{{{{item.display_name:call:}}}}, }}|
Classification|{{item.maxClassification}}|
Finding Count|{{item:call:getFindingCount}}|

{{item.findings:if:

**Threats**

{{item.findings:repeat:
<details>
  <summary>   {{{{item.id}}}}  --  {{{{item.threat_id}}}}   --   {{{{item.description}}}}</summary>
  <h6> Targeted Element </h6>
  <p> {{{{item.target}}}} </p>
  <h6> Severity </h6>
  <p>{{{{item.severity}}}}</p>
  <h6>Example Instances</h6>
  <p>{{{{item.example}}}}</p>
  <h6>Mitigations</h6>
  <p>{{{{item.mitigations}}}}</p>
  <h6>References</h6>
  <p>{{{{item.references}}}}</p>
  &emsp;
</details>
}}
}}
}

## Assets 

{assets:repeat:
Name|{{item.name}}|
|:----|:----|
Description|{{item.description}}|
In Scope|{{item.inScope}}|
Type|{{item:call:getElementType}}|
Finding Count|{{item:call:getFindingCount}}|

{{item.findings:if:

**Threats**

{{item.findings:repeat:
<details>
  <summary>   {{{{item.id}}}}  --  {{{{item.threat_id}}}}   --   {{{{item.description}}}}</summary>
  <h6> Targeted Element </h6>
  <p> {{{{item.target}}}} </p>
  <h6> Severity </h6>
  <p>{{{{item.severity}}}}</p>
  <h6>Example Instances</h6>
  <p>{{{{item.example}}}}</p>
  <h6>Mitigations</h6>
  <p>{{{{item.mitigations}}}}</p>
  <h6>References</h6>
  <p>{{{{item.references}}}}</p>
  &nbsp;
</details>
}}
}}
}

## Data Flows 

{dataflows:repeat:
Name|{{item.name}}
|:----|:----|
Description|{{item.description}}|
Sink|{{item.sink}}|
Source|{{item.source}}|
Is Response|{{item.isResponse}}|
In Scope|{{item.inScope}}|
Finding Count|{{item:call:getFindingCount}}|

{{item.findings:if:

**Threats**

{{item.findings:repeat:
<details>
  <summary>   {{{{item.id}}}}  --  {{{{item.threat_id}}}}   --   {{{{item.description}}}}</summary>
  <h6> Targeted Element </h6>
  <p> {{{{item.target}}}} </p>
  <h6> Severity </h6>
  <p>{{{{item.severity}}}}</p>
  <h6>Example Instances</h6>
  <p>{{{{item.example}}}}</p>
  <h6>Mitigations</h6>
  <p>{{{{item.mitigations}}}}</p>
  <h6>References</h6>
  <p>{{{{item.references}}}}</p>
  &emsp;
</details>
}}
}}
}
