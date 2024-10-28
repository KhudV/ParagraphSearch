from interface import IndexRequest, ProcessedIndexingRequest



def process(
        request_sp: IndexRequest
    ) -> ProcessedIndexingRequest:
        print('call convert with:', request_sp.__dict__)
        # print('---->', request_sp.content)
        # return None
        return ProcessedIndexingRequest(
                content = request_sp.content,
                vector  = [7, 1, 7]
        )
