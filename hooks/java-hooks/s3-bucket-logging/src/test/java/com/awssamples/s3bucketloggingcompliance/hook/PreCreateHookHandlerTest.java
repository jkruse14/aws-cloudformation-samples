package com.awssamples.s3bucketloggingcompliance.hook;

import java.util.Map;
import java.util.HashMap;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class PreCreateHookHandlerTest extends AbstractTestBase {

    @Mock
    private AmazonWebServicesClientProxy proxy;

    @Mock
    private Logger logger;

    @BeforeEach
    public void setup() {
        proxy = mock(AmazonWebServicesClientProxy.class);
        logger = mock(Logger.class);
    }

    @Test
    public void handleRequest_SimpleSuccess() {
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().loggingBucket("BucketName").build();

        final Map<String, Object> targetModel = new HashMap<>();
        final Map<String, Object> resourceProperties = new HashMap<>();
        final Map<String, Object> loggingConfiguration = new HashMap<>();
        loggingConfiguration.put("DestinationBucketName", "BucketName");
        resourceProperties.put("LoggingConfiguration", loggingConfiguration);
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getErrorCode()).isNull();
    }

    @Test
    public void handleRequest_NoBucketPropertiesFailure() {
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().loggingBucket("BucketName").build();

        final Map<String, Object> targetModel = new HashMap<>();

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    @Test
    public void handleRequest_NoBucketLoggingFailure() {
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().loggingBucket("BucketName").build();

        final Map<String, Object> targetModel = new HashMap<>();
        final Map<String, Object> resourceProperties = new HashMap<>();
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);
        
        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    @Test
    public void handleRequest_BucketNameDoesntMatchFailure() {
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().loggingBucket("BucketName").build();

        final Map<String, Object> targetModel = new HashMap<>();
        final Map<String, Object> resourceProperties = new HashMap<>();
        final Map<String, Object> loggingConfiguration = new HashMap<>();
        loggingConfiguration.put("DestinationBucketName", "WrongName");
        resourceProperties.put("LoggingConfiguration", loggingConfiguration);
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::S3::Bucket").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }
}