package function

import (
	faasflow "github.com/faasflow/lib/openfaas"
)

// Define provide definition of the workflow
func Define(flow *faasflow.Workflow, context *faasflow.Context) (err error) {
	// myOptions := faasflow.Options{
	// 	header: map[string]string{
	// 		"Content-Type": "application/json",
	// 	},
	// 	query: map[string][]string{
	// 		"string1": {"value1"},
	// 		"string2": {"value2"},
	// 	},
	// }

	flow.SyncNode().Apply("func1").Apply("func2").
		Modify(func(data []byte) ([]byte, error) {
			data = []byte(string(data) + "modifier")
			return data, nil
		})
	return
}

// OverrideStateStore provides the override of the default StateStore
func OverrideStateStore() (faasflow.StateStore, error) {
	// NOTE: By default FaaS-Flow use consul as a state-store,
	//       This can be overridden with other synchronous KV store (e.g. ETCD)
	return nil, nil
}

// OverrideDataStore provides the override of the default DataStore
func OverrideDataStore() (faasflow.DataStore, error) {
	// NOTE: By default FaaS-Flow use minio as a data-store,
	//       This can be overridden with other synchronous KV store
	return nil, nil
}
